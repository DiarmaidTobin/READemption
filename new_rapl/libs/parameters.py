class Parameters(object):
    segemehl_accuracy = 95    # Must be an int (due to Segemehl)
    segemehl_hit_strategy = 1
    segemehl_max_e_value = 5.0
    segemehl_number_of_threads = 20
    python_number_of_threads = 20

    # This define how expection should be treated exspecilly the once
    # that run in parellel. The option are "report" or "crash"
    # - report: The exceptions are written to stderr but the program
    #           should continue
    # - crash: the exception is raised
    exception_handling = "report"
    # Filtering
    min_seq_length = 12
    min_overlap = 10
    min_read_overlap_perc = 0.0
    uniquely_mapped_reads_only = False

