// FIXME
//throttle(['Gerrit']) {
//}

def main() {
    def test_gerrit_helper = load("${checkout_dir}/buildscripts/scripts/utils/gerrit_stages.groovy");
    def result_dir = "${checkout_dir}/results";
    def issues = [];
    def time_job_started = new Date();
    def time_stage_started = time_job_started;

    print(
        """
        |===== CONFIGURATION ===============================
        |GERRIT_PATCHSET_REVISION:.(global)  │${GERRIT_PATCHSET_REVISION}│
        |GERRIT_CHANGE_SUBJECT:....(global)  │${GERRIT_CHANGE_SUBJECT}│
        |GERRIT_BRANCH:............(global)  │${GERRIT_BRANCH}│
        |===================================================
        """.stripMargin());

    withCredentials([
        usernamePassword(
            credentialsId: 'nexus',
            passwordVariable: 'DOCKER_PASSPHRASE',
            usernameVariable: 'DOCKER_USERNAME')]) { 
        sh('echo  "${DOCKER_PASSPHRASE}" | docker login "${DOCKER_REGISTRY}" -u "${DOCKER_USERNAME}" --password-stdin');
    }

    time_stage_started = test_gerrit_helper.log_stage_duration(time_stage_started);

    /// Add description to the build
    test_gerrit_helper.desc_init();
    test_gerrit_helper.desc_add_line("${GERRIT_CHANGE_SUBJECT}");
    test_gerrit_helper.desc_add_table();
    test_gerrit_helper.desc_add_row('Stage', 'Duration', 'Status', 'Result files');

    stage("Prepare workspace") {
        dir("${checkout_dir}") {
            sh("rm -rf ${result_dir}; mkdir ${result_dir}")

            /// Reason for the following try/catch block:
            /// Jenkins will abort jobs (e.g. in case of a new patch set) with SIGKILL (at least this is what we think)
            /// in case a job is aborted during a rebuild of the .venv, the .venv will be left broken
            /// the next run in this workspace will use the .venv as-is but fail to import modules
            /// attempts to use a trap in the .venv Makefile-target were also not succesful - SIGKILL is not trap-able...
            /// So at the end, we need to use a groovy try/catch to ensure a rebuild in the next job in case something failed
            try {
                docker_image_from_alias("IMAGE_TESTING").inside() {
                    withEnv(["PIPENV_VERBOSE=1"]) {
                        sh("make .venv");
                    }
                }
            } catch (e) {
                sh("rm -rf .venv");
                throw e;
            }
        }
        time_stage_started = test_gerrit_helper.log_stage_duration(time_stage_started);
    }
    try {

        dir("${checkout_dir}") {
            stage("Create stages") {
                /// Generate list of stages to be added - save them locally for reference
                sh("""scripts/run-in-docker.sh \
                    scripts/run-pipenv run \
                      buildscripts/scripts/validate_changes.py \
                      --env "RESULTS=${result_dir}" \
                      --env "WORKSPACE=${checkout_dir}" \
                      --env "PATCHSET_REVISION=${GERRIT_PATCHSET_REVISION}" \
                      --write-file=${result_dir}/stages.json \
                      buildscripts/scripts/stages.yml
                """);

                time_stage_started = test_gerrit_helper.log_stage_duration(time_stage_started);
            }
            test_gerrit_helper.desc_add_status_row("Preparation",
                groovy.time.TimeCategory.minus(new Date(), time_job_started), 0, '--');

            def stage_info = load_json("${result_dir}/stages.json");
            def allStagesPassed = true;
            stage_info.STAGES.each { item ->
                allStagesPassed = test_gerrit_helper.create_stage(item, issues, time_stage_started) and allStagesPassed;
                sh("ls -alF ${result_dir}");
                time_stage_started = test_gerrit_helper.log_stage_duration(time_stage_started);
            }
            currentBuild.result = allStagesPassed ? "SUCCESS" : "FAILED";
        }
    } finally {
        test_gerrit_helper.desc_add_line("Executed on: ${NODE_NAME} in ${WORKSPACE}");
        stage("Analyse Issues") {
            if (issues) {
                publishIssues(
                    issues: issues,
                    trendChartType: 'TOOLS_ONLY',
                    qualityGates: [[threshold: 1, type: 'TOTAL', unstable: false]]);
            }
            dir("${checkout_dir}") {
                xunit([
                    Custom(
                        customXSL: "$JENKINS_HOME/userContent/xunit/JUnit/0.1/pytest-xunit.xsl",
                        deleteOutputFiles: false,
                        failIfNotNew: true,
                        pattern: "results/*junit.xml",
                        skipNoTestFiles: true,
                        stopProcessingIfError: true,
                )])

                archiveArtifacts(allowEmptyArchive: true, artifacts: 'results/*');
            }
        }
        time_stage_started = test_gerrit_helper.log_stage_duration(time_stage_started);
    }
}
return this;

