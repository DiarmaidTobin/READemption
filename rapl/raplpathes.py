class RaplPathes(object):

    def __init__(self):
        self._set_folder_names()
        self._set_file_names()

    def _set_folder_names(self):
        """Set the name of folders used in a project."""
        self.input_folder = "input"
        self.output_folder = "output"
        self.rna_seq_folder = "%s/RNA_seqs" % self.input_folder
        self.genome_folder = "%s/genomes" % self.input_folder
        self.input_file_stats_folder = "%s/input_file_stats" % self.output_folder
        self.annotation_folder = "%s/annotation_files" % self.input_folder
        self.read_mappings_first_run_folder = "%s/read_mappings_first_run" % (
            self.output_folder)
        self.read_mappings_second_run_folder = (
            "%s/read_mappings_second_run" % self.output_folder)
        self.gr_folder = "%s/gr_files" % self.output_folder
        self.gr_folder_read_normalized = "%s/gr_read_normalized_files" % (
            self.output_folder)
        self.gr_folder_nucl_normalized = "%s/gr_nucleotide_normalized_files" % (
            self.output_folder)
        self.read_mapping_index_folder = "%s/read_mapping_index" % (
            self.output_folder)
        self.umapped_reads_of_first_mapping_folder = (
            "%s/unmapped_reads_of_first_mapping" % self.output_folder)
        self.umapped_reads_of_second_mapping_folder = (
            "%s/unmapped_reads_of_second_mapping" % self.output_folder)
        self.combined_mappings_folder = "%s/read_mappings_combined" % (
            self.output_folder)
        self.combined_mapping_split_folder = (
            "%s/read_mappings_combined_split_by_genome_files" % 
            self.output_folder)
        self.annotation_hit_folder = "%s/annotation_hits" % self.output_folder
        self.annotation_hit_overview_folder = (
            "%s/annotation_hit_overviews" % self.output_folder)
        self.annotation_hit_overview_read_normalized_folder = (
            "%s/annotation_hit_overviews_read_normalized" % self.output_folder)
        self.annotation_hit_overview_nucl_normalized_folder = (
            "%s/annotation_hit_overviews_nucleotide_normalized" % 
            self.output_folder)
        self.read_tracing_folder = "%s/read_tracing" % (self.output_folder)
        self.report_folder = "%s/reports_and_stats" % (self.output_folder)

    def _set_file_names(self):
        """Set name of common files."""
        self.config_file = "rapl.config"
        self.read_file_stats = "%s/read_file_stats.txt" % (
            self.input_file_stats_folder)
        self.genome_file_stats = "%s/genome_file_stats.txt" % (
            self.input_file_stats_folder)
        self.annotation_file_stats = "%s/annotation_file_stats.txt" % (
            self.input_file_stats_folder)
        self.tracing_summary_file = "%s/read_tracing_summary.csv" % (
            self.report_folder)
        self.report_tex_file = "%s/report.tex" % (
            self.report_folder)
        self.lib_genome_read_mapping_summary = (
            "%s/read_coutings_per_genome_file.cvs" % (self.report_folder))

    def required_folders(self):
        return([self.input_folder, self.output_folder, self.rna_seq_folder,
                self.annotation_folder, self.read_mappings_first_run_folder,
                self.read_mappings_second_run_folder, self.gr_folder,
                self.gr_folder_read_normalized, self.gr_folder_nucl_normalized,
                self.read_mapping_index_folder, self.genome_folder,
                self.umapped_reads_of_first_mapping_folder,
                self.umapped_reads_of_second_mapping_folder,
                self.combined_mappings_folder, self.combined_mapping_split_folder,
                self.annotation_hit_folder, self.annotation_hit_overview_folder,
                self.annotation_hit_overview_read_normalized_folder,
                self.annotation_hit_overview_nucl_normalized_folder,
                self.read_tracing_folder, self.input_file_stats_folder, 
                self.report_folder])
    

    def _read_file_path(self, read_file):
        """Return the full path of a given read file.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s" % (self.rna_seq_folder, read_file))

    def _unmapped_raw_read_file_path(self, read_file):
        """Return the full path of unmapped reads of the first run.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.unmapped.fa" % (
                self.umapped_reads_of_first_mapping_folder, read_file))

    def _segemehl_index_path(self):
        """Return the full path the the in segemehl index file."""
        return("%s/%s"  % (
                self.read_mapping_index_folder, self._segemehl_index_name()))

    def _genome_file_path(self, genome_file):
        """Return the ull path of a given genome file

        Arguments:
        - `genome_file`: genome file name
        """
        return("%s/%s" % (self.genome_folder, genome_file))

    def _genome_file_paths(self):
        """Return the full paths of all genome files"""
        return([self._genome_file_path(genome_file) 
                for genome_file in self.genome_files])

    def _raw_read_mapping_output_path(self, read_file):
        """Return the full path of the output file of a segemehl run

        Arguments:
        - `read_file`: read file name that is mapped
        """
        return("%s/%s_mapped_to_%s" % (
                self.read_mappings_first_run_folder, read_file, self._segemehl_index_name()))

    def _unmapped_read_clipped_path(self, read_file):
        """Return the full path of a file with clipped reads

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.unmapped.fa.clipped.fa" % (
                self.umapped_reads_of_first_mapping_folder, read_file))


    def _unmapped_clipped_size_filtered_read_path(self, read_file):
        """Return the full path of clipped and size filtered reads.

        Arguments:
        - `read_file`: name of the read file

        """
        return("%s/%s.unmapped.fa.clipped.fa.size_filtered_gtoe_%sbp.fa" % (
                self.umapped_reads_of_first_mapping_folder,
                read_file, self.min_seq_length))

    def _clipped_reads_mapping_output_path(self, read_file):
        """Return the path of the mapping file of the second run.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.clipped_mapped_to_%s" % (
                self.read_mappings_second_run_folder,
                read_file, self._segemehl_index_name()))

    def _unmapped_reads_of_clipped_reads_file_path(self, read_file):
        """Return the full path of the unmapped reads of the 2nd run.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.unmapped.fa"  % (self.umapped_reads_of_first_mapping_folder, 
                           read_file))

    def _unmapped_reads_second_mapping_path(self, read_file):
        """Return the path of unmapped reads of the second run.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.unmapped.fa" % (
                self.umapped_reads_of_second_mapping_folder, read_file))

    def _combined_mapping_file_path(self, read_file):
        """Return the path of the combined mappings.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s_mapped_to_%s.combined" % (
                self.combined_mappings_folder, read_file,
                self._segemehl_index_name()))

    def _combined_mapping_file_a_filtered_split_path(self, read_file, genome_file):
        """Return the path of the split filtered combined mappings.
        
        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s_mapped_to_%s.combined.filtered_ltoe_%s%%_A.txt.from_%s_only" % (
                self.combined_mapping_split_folder, read_file, 
                self._segemehl_index_name(), self.max_a_content, genome_file))

    def _combined_mapping_file_a_filtered_path(self, read_file):
        """Return the path of the filtered combined mappings.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s.filtered_ltoe_%s%%_A.txt" % (
                self._combined_mapping_file_path(read_file),
                self.max_a_content))

    def _unmapped_clipped_size_failed_read_path(self, read_file):
        """Return the path of size filter failed clipped reads.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.unmapped.fa.clipped.fa.size_filtered_lt_%sbp.fa" % (
                self.umapped_reads_of_first_mapping_folder,
                read_file, self.min_seq_length))

    def _combined_mapping_file_a_filter_failed_path(self, read_file):
        """Return the path of the A-content filter failed reads.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s.filtered_gt_%s%%_A.txt" % (
                self._combined_mapping_file_path(read_file),
                self.max_a_content))

    def _trace_file_path(self, read_file):
        """Return the path of the trace file of a read file.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.mapping_tracing.csv" % (
                self.read_tracing_folder, read_file))

    def _gr_file_path(self, read_file, genome_file):
        """Return the GR file path of a given read and genome file.

        Arguments:
        - `read_file,`: name of the read file
        - `genome_file`: name of the genome file
        """
        return("%s/%s_in_%s.gr" % (self.gr_folder, read_file, genome_file))

    def _gr_read_normalized_file_path(self, read_file, genome_file):
        """Return the GR read normalized file path of a given read and
        genome file.

        Arguments:
        - `read_file,`: name of the read file
        - `genome_file`: name of the genome file
        """
        return("%s/%s_in_%s.gr" % (
                self.gr_folder_read_normalized, read_file, genome_file))

    def _gr_nucl_normalized_file_path(self, read_file, genome_file):
        """Return the GR nucleotide normalized file path of a given read and
        genome file.

        Arguments:
        - `read_file,`: name of the read file
        - `genome_file`: name of the genome file
        """
        return("%s/%s_in_%s.gr" % (
                self.gr_folder_nucl_normalized, read_file, genome_file))

    def _annotation_hit_file_path(self, read_file, annotation_file):
        """Return the path of the annoation hit file.

        Arguments:
        - `read_file,`: name of the read file
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s_in_%s_annotation_hits" % (
                self.annotation_hit_folder, read_file, annotation_file))

    def _annotation_file_path(self, annotation_file):
        """Return the path of a given annotation files.

        Arguments:
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s" % (self.annotation_folder , annotation_file))

    def _annotation_hit_overview_file_path(self, annotation_file):
        """Return the path of the annotation overview file.

        Arguments:
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s_all_annotation_hits_sense.csv" % (
                self.annotation_hit_overview_folder, annotation_file))

    def _annotation_hit_overview_antisense_file_path(self, annotation_file):
        """Return the path of the annotation overview file for antisense hits.

        Arguments:
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s_all_annotation_hits_antisense.csv" % (
                self.annotation_hit_overview_folder, annotation_file))

    def _annotation_hit_overview_read_normalized_file_path(self, annotation_file):
        """Return the path of the annotation overview normalized by
           mapped reads file.
        """
        return("%s/%s_all_annotation_hits_normalized_by_reads_sense.csv" % (
                self.annotation_hit_overview_read_normalized_folder, 
                annotation_file))

    def _annotation_hit_overview_read_normalized_antisense_file_path(self, annotation_file):
        """Return the path of the annotation overview normalized by
           mapped reads file.
        """
        return("%s/%s_all_annotation_hits_normalized_by_reads_antisense.csv" % (
                self.annotation_hit_overview_read_normalized_folder, 
                annotation_file))

    def _annotation_hit_overview_nucl_normalized_file_path(self, annotation_file):
        """Return the path of the annotation overview normalized by
           mapped nucleotides file.
        """
        return("%s/%s_all_annotation_hits_normalized_by_nucleotides_sense.csv" % (
                self.annotation_hit_overview_nucl_normalized_folder, 
                annotation_file))

    def _annotation_hit_overview_nucl_normalized_antisense_file_path(self, annotation_file):
        """Return the path of the annotation overview normalized by
           mapped nucleotides file.
        """
        return("%s/%s_all_annotation_hits_normalized_by_nucleotides_antisense.csv" % (
                self.annotation_hit_overview_nucl_normalized_folder, 
                annotation_file))
