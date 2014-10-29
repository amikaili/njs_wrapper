module NJSMock {

    /* @range [0,1] */
    typedef int boolean;

    typedef structure {
        string service_url;
        string method_name;
    } generic_service_method;

    typedef structure {
        string python_class;
        string method_name;
    } python_backend_method;

    typedef structure {
        string script_name;
    } commandline_script_method;

    /*
        type - 'generic', 'python' or 'script'.
        job_id_output_field - this field is used only in case this step is long running job and
            output of service method is structure with field having name coded in 
            'job_id_output_field' rather than just output string with job id.
    */
    typedef structure {
        string step_id;
        string type;
        generic_service_method generic;
        python_backend_method python;
        commandline_script_method script;
        list<UnspecifiedObject> input_values;
        boolean is_long_running;
        string job_id_output_field;
    } step;

    typedef structure {
        list<step> steps;
    } app;

    /*
        step_job_ids - mapping from step_id to job_id.
    */
    typedef structure {
        string app_job_id;
        string running_step_id;
        mapping<string, string> step_job_ids;
        mapping<string, UnspecifiedObject> step_outputs;
    } app_state;

    funcdef run_app(app app) returns (app_state) authentication required;

    funcdef check_app_state(string app_job_id) returns (app_state) authentication required;

};
