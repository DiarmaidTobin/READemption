import os
from rapl.parameters import Parameters

class Paths(object):

    def __init__(self):
        self._set_folder_names()
        self._set_file_names()
        self._set_bin_paths()
        self._get_read_file_names()
        self._get_genome_file_names()
        self.parameters = Parameters()

    def _set_folder_names(self):
        """Set the name of folders used in a project."""
        self.input_folder = "input"
        self.output_folder = "output"
        self.rna_seq_folder = "%s/RNA_seqs" % self.input_folder
        self.genome_folder = "%s/genomes" % self.input_folder
        self.input_file_stats_folder = "%s/input_file_stats" % self.output_folder
        self.annotation_folder = "%s/annotation_files" % self.input_folder
        self.gr_folder = "%s/gr_files" % self.output_folder
        self.gr_folder_read_normalized = "%s/gr_read_normalized_files" % (
            self.output_folder)
        self.gr_folder_nucl_normalized = "%s/gr_nucleotide_normalized_files" % (
            self.output_folder)
        self.read_mapping_index_folder = "%s/read_mapping_index" % (
            self.output_folder)
        self.annotation_hit_folder = "%s/annotation_hits" % self.output_folder
        self.no_annotation_hit_folder = "%s/without_annotation_hits" % self.output_folder
        self.annotation_hit_overview_folder = (
            "%s/annotation_hit_overviews" % self.output_folder)
        self.annotation_hit_overview_read_normalized_folder = (
            "%s/annotation_hit_overviews_read_normalized" % self.output_folder)
        self.annotation_hit_overview_nucl_normalized_folder = (
            "%s/annotation_hit_overviews_nucleotide_normalized" % 
            self.output_folder)
        self.annotation_hit_overview_rpkm_normalized_folder = (
            "%s/annotation_hit_overviews_rpkm_normalized" % 
            self.output_folder)
        self.read_tracing_folder = "%s/read_tracing" % (self.output_folder)
        self.report_folder = "%s/reports_and_stats" % (self.output_folder)

        self.read_mappings_folder = "%s/read_mappings" % (
            self.output_folder)
        self.clipped_reads_folder = "%s/clipped_reads" % (
            self.output_folder)
        self.unmapped_reads_folder = "%s/unmapped_reads" % (
            self.output_folder)

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
            "%s/mapping_and_mapped_read_coutings_per_genome_file.csv" % (
                self.report_folder))
        self.mapping_length_hist_r_file = (
            "%s/mapping_length_distributions.R" % self.report_folder)
        self.mapping_length_hist_pdf_file = (
            "%s/mapping_length_distributions.pdf" % self.report_folder)

    def _get_read_file_names(self):
        """Read the names of the read files."""
        if os.path.exists(self.rna_seq_folder):
            self.read_files = sorted(os.listdir(self.rna_seq_folder))
        else:
            self.read_files = []

    def _get_genome_file_names(self):
        """Read the names of genome files."""
        if os.path.exists(self.genome_folder):
            self.genome_files = sorted(os.listdir(self.genome_folder))
        else:
            self.genome_files = []

    def _set_bin_paths(self):
        """Set file/folder paths for some needed binaries."""
        #self.segemehl_bin = "segemehl"
        self.segemehl_bin = "segemehl_dev"
        # DEV
        self.python_bin = "/opt/Python-3.2/python"
        self.bin_folder = (os.path.split(os.path.realpath(__file__))[0] + 
                           "/rapl_tools")
    def required_folders(self):
        return([self.input_folder, self.output_folder, self.rna_seq_folder,
                self.annotation_folder,              
                self.gr_folder, self.gr_folder_read_normalized, 
                self.gr_folder_nucl_normalized, self.read_mappings_folder,
                self.clipped_reads_folder, self.unmapped_reads_folder,
                self.read_mapping_index_folder, self.genome_folder,
                self.annotation_hit_folder, self.annotation_hit_overview_folder,
                self.annotation_hit_overview_read_normalized_folder,
                self.annotation_hit_overview_nucl_normalized_folder,
                self.annotation_hit_overview_rpkm_normalized_folder,
                self.read_tracing_folder, self.input_file_stats_folder, 
                self.report_folder, self.no_annotation_hit_folder])
    

    def read_file(self, read_file):
        """Return the full path of a given read file.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s" % (self.rna_seq_folder, read_file))

    def segemehl_index(self):
        """Return the full path the the in segemehl index file."""
        return("%s/%s"  % (
                self.read_mapping_index_folder, self.segemehl_index_name()))

    def genome_file(self, genome_file):
        """Return the full path of a given genome file

        Arguments:
        - `genome_file`: genome file name
        """
        return("%s/%s" % (self.genome_folder, genome_file))

    def genome_file_paths(self):
        """Return the full paths of all genome files"""
        return([self.genome_file(genome_file) 
                for genome_file in self.genome_files])

    def clipped_read_file_prefix(self, read_file):
        """Return the full path of a file with clipped reads

        Arguments:
        - `read_file`: name of the read file
        """
        # ".clipped.fa" will be added by the tool
        return("%s/%s" % (self.clipped_reads_folder, read_file))

    def clipped_read_file(self, read_file):
        """Return the full path of a file with clipped reads

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.clipped.fa" % (self.clipped_reads_folder, read_file))

    def clipped_read_file(self, read_file):
        """Return the full path of a file with clipped reads

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.clipped.fa" % (self.clipped_reads_folder, read_file))

    def clipped_size_filtered_read_file(self, read_file):
        """Return the full path of a file clipped, size filtered reads

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s.size_filtered_gtoe_%sbp.fa" % (
                self.clipped_read_file(read_file),
                self.parameters.min_seq_length))

    def clipped_size_filter_failed_read_file(self, read_file):
        """Return the full path of a file with clipped but too short reads.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s.size_filtered_lt_%sbp.fa" % (
                self.clipped_read_file(read_file),
                self.parameters.min_seq_length))

    def read_mapping_output_file(self, read_file):
        """Return the full path of the output file of a segemehl run

        Arguments:
        - `read_file`: read file name that is mapped
        """
        return("%s/%s_mapped_to_%s" % (
                self.read_mappings_folder, read_file, self.segemehl_index_name()))

    def unmapped_reads_file(self, read_file):
        """Return the full path of a file with unmapped reads

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.clipped.fa.unmapped" % (
                self.unmapped_reads_folder, read_file))

    def a_filtered_mappings_file(self, read_file):
        """Return the full path of a file with a filterd mappings

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s.filtered_ltoe_70.0%%_A.txt" % (
                self.read_mapping_output_file(read_file)))

    def a_filter_failed_mappings_file(self, read_file):
        """Return the full path of a file with a filterd mappings

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s.filtered_gt_70.0%%_A.txt" % (
                self.read_mapping_output_file(read_file)))

    def unique_mappings_only_file(self, read_file):
        """ Return the path of the file with unique mappings only

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s.unique_mappings_only" % (
                self.a_filtered_mappings_file(read_file)))

    def trace_file(self, read_file):
        """Return the path of the trace file of a read file.

        Arguments:
        - `read_file`: name of the read file
        """
        return("%s/%s.mapping_tracing.csv" % (
                self.read_tracing_folder, read_file))

    def gr_file(self, read_file, genome_file):
        """Return the GR file path of a given read and genome file.

        Arguments:
        - `read_file,`: name of the read file
        - `genome_file`: name of the genome file
        """
        return("%s/%s_in_%s.gr" % (self.gr_folder, read_file, genome_file))

    def gr_read_normalized_file(self, read_file, genome_file):
        """Return the GR read normalized file path of a given read and
        genome file.

        Arguments:
        - `read_file,`: name of the read file
        - `genome_file`: name of the genome file
        """
        return("%s/%s_in_%s.gr" % (
                self.gr_folder_read_normalized, read_file, genome_file))

    def gr_nucl_normalized_file(self, read_file, genome_file):
        """Return the GR nucleotide normalized file path of a given read and
        genome file.

        Arguments:
        - `read_file,`: name of the read file
        - `genome_file`: name of the genome file
        """
        return("%s/%s_in_%s.gr" % (
                self.gr_folder_nucl_normalized, read_file, genome_file))

    def annotation_hit_file(self, read_file, annotation_file):
        """Return the path of the annoation hit file.

        Arguments:
        - `read_file,`: name of the read file
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s_in_%s_annotation_hits" % (
                self.annotation_hit_folder, read_file, annotation_file))

    def annotation_hit_file_with_mapping_coutings(
        self, read_file, annotation_file):
        """Return the path of the annoation hit file with number of mappings

        Arguments:
        - `read_file,`: name of the read file
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return(self.annotation_hit_file(read_file, annotation_file) + 
               "_with_mapping_countings")

    def annotation_file(self, annotation_file):
        """Return the path of a given annotation files.

        Arguments:
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s" % (self.annotation_folder , annotation_file))

    def annotation_hit_overview_file(self, annotation_file):
        """Return the path of the annotation overview file.

        Arguments:
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s_all_annotation_hits_sense.csv" % (
                self.annotation_hit_overview_folder, annotation_file))

    def annotation_hit_overview_antisense_file(self, annotation_file):
        """Return the path of the annotation overview file for antisense hits.

        Arguments:
        - `annotation_file`: name of the (NCBI) annotation file
        """
        return("%s/%s_all_annotation_hits_antisense.csv" % (
                self.annotation_hit_overview_folder, annotation_file))

    def annotation_hit_overview_read_normalized_file(self, annotation_file):
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

    def annotation_hit_overview_nucl_normalized_file(self, annotation_file):
        """Return the path of the annotation overview normalized by
           mapped nucleotides file.
        """
        return("%s/%s_all_annotation_hits_normalized_by_nucleotides_sense.csv" % (
                self.annotation_hit_overview_nucl_normalized_folder, 
                annotation_file))

    def annotation_hit_overview_nucl_normalized_antisense_file(self, annotation_file):
        """Return the path of the annotation overview normalized by
           mapped nucleotides file.
        """
        return("%s/%s_all_annotation_hits_normalized_by_nucleotides_antisense.csv" % (
                self.annotation_hit_overview_nucl_normalized_folder, 
                annotation_file))

    def annotation_hit_overview_rpkm_normalized_file(self, annotation_file):
        """Return the path of the RPKM normalized annotation overview

        """
        return("%s/%s_all_annotation_hits_normalized_by_rpkm_sense.csv" % (
                self.annotation_hit_overview_rpkm_normalized_folder, 
                annotation_file))

    def annotation_hit_overview_rpkm_normalized_antisense_file(self, annotation_file):
        """Return the path of the RPKM normalized annotation.
        """
        return("%s/%s_all_annotation_hits_normalized_by_rpkm_antisense.csv" % (
                self.annotation_hit_overview_rpkm_normalized_folder, 
                annotation_file))

    def no_annotation_hit_file(self, read_file, genome_file):
        """Return the path of a file containing reads without
        annotation overlap
        """
        return("%s/%s_in_%s_reads_without_annotation" % (
                self.no_annotation_hit_folder, read_file, 
                genome_file))

    def segemehl_index_name(self):
        """Return the name of the segemehl index file."""
        # TODO Avoid too long file name later.
        #index_file_name = "_".join(self.genome_files) + ".idx"
        #index_file_name.replace(".fa", "")
        index_file_name = "genome.idx"
        return(index_file_name)

    def final_filtered_mapping_file(self, read_file):
        """Return the final filtered mapping file.
        
        Depending of all or only uniquely mapped read mappings should
        be considered.
        """
        if self.parameters.uniquely_mapped_reads_only:
            return(self.unique_mappings_only_file(read_file))
        return(self.a_filtered_mappings_file(read_file))
