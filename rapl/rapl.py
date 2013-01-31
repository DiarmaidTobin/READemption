#!/usr/bin/env python

"""RAPL - A RNA-seq Analysing PipeLine"""

import argparse
from libs.controller import Controller

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands")

    # Arguments for project creation
    start_project_parser = subparsers.add_parser(
        "start", help="Start a project")
    start_project_parser.add_argument(
        "project_path", default=".", help="Name/path of the project.")
    start_project_parser.set_defaults(func=start_project)

    # Parameters for read mapping
    read_mapping_parser = subparsers.add_parser(
        "map", help="Run read mappings")
    read_mapping_parser.add_argument(
        "project_path", default=".", nargs="?",
        help="Path of the project folder. If none is given the current "
        "directory is used.")
    read_mapping_parser.add_argument(
        "--min_read_length", "-l", default=12, type=int,
        help="Minimal read length after clipping")
    read_mapping_parser.add_argument(
        "--threads", "-t", default=1, type=int,
        help="Number of threads that should be used.")
    # read_mapping_parser.add_argument(
    #     "--force", "-f", default=False, action="store_true",
    #     help="Overwrite existing files.")
    read_mapping_parser.add_argument(
        "--segemehl_accuracy", "-a", default=95.0, type=float,
        help="Segemehl's minimal accuracy (in %%) (default 95).")
    read_mapping_parser.add_argument(
        "--segemehl_evalue", "-e", default=5.0, type=float,
        help="Segemehl's maximal e-value. (default 5.0)")
    read_mapping_parser.add_argument(
        "--segemehl_bin", "-s", default="segemehl",
        help="segemehl's binary path.")
    read_mapping_parser.set_defaults(func=map_reads)

    # Parameters for coverage file building
    coverage_creation_parser = subparsers.add_parser(
        "coverage", help="Create coverage (wiggle) files")
    coverage_creation_parser.add_argument(
        "project_path", default=".", nargs="?",
        help="Path of the project folder. If none is given the current "
        "directory is used.")
    coverage_creation_parser.add_argument(
        "--unique_only", "-u", default=False, action="store_true",
        help="Use uniquely mapped reads only.")
    # coverage_creation_parser.add_argument(
    #     "--force", "-f", default=False, action="store_true",
    #     help="Overwrite existing files.")
    coverage_creation_parser.set_defaults(func=create_coverage_files)
    coverage_creation_parser.add_argument(
        "--threads", "-t", default=1, type=int,
        help="Number of threads that should be used.")
    coverage_creation_parser.add_argument(
        "--skip_read_count_splitting", "-s", default=False,
        action="store_true", help="Do not split the read counting between "
        "different mappings. Default is to do the splitting.")

    # Parameters for gene wise quantification
    gene_wise_quanti_parser = subparsers.add_parser(
        "gene_quanti", help="Quantify the expression gene wise")
    gene_wise_quanti_parser.add_argument(
        "project_path", default=".", nargs="?",
        help="Path of the project folder. If none is given the current "
        "directory is used.")
    gene_wise_quanti_parser.add_argument(
        "--min_overlap", "-o", default=1, type=int,
        help="Minimal read-annotation-overlap (in nt) (default 1)")
    gene_wise_quanti_parser.add_argument(
        "--skip_norm_by_mapping_freq", default=False)
    gene_wise_quanti_parser.add_argument(
        "--skip_norm_by_overlap_freq", default=False)
    gene_wise_quanti_parser.set_defaults(func=run_gene_wise_quantification)
    # - uniquely only
    # - skip antisense
    # - use gene overlap normalizatoin
    # - use mapping normalization
    # - --force (see above)
    # - use only given features (gene, exon, region)
    # - discard feature in certain lenght range (can help
    #   indirectly remove "region")

    # Obsolete
    # Parameters for annotation overlap searches
    # annotation_overlap_parser = subparsers.add_parser(
    #     "annotate", help="Search annoation overlaps")
    # annotation_overlap_parser.add_argument(
    #     "project_path", default=".", nargs="?",
    #     help="Path of the project folder. If none is given the current "
    #     "directory is used.")
    # annotation_overlap_parser.add_argument(
    #     "--threads", "-t", default=1, type=int,
    #     help="Number of threads that should be used.")

    # TODO
    # annotation_overlap_parser.add_argument(
    #     "--force", "-f", default=False, action="store_true",
    #     help="Overwrite existing files.")
    #annotation_overlap_parser.set_defaults(func=search_annotation_overlaps)

    # Obsolete
    # Parameters for annotation overlap overviews
    # annotation_overview_parser = subparsers.add_parser(
    #     "annotation_overview", help="Create annotation overlap overviews")
    # annotation_overview_parser.add_argument(
    #     "project_path", default=".", nargs="?",
    #     help="Path of the project folder. If none is given the current "
    #     "directory is used.")
    # annotation_overview_parser.add_argument(
    #     "--min_overlap", "-o", default=10, type=int,
    #     help="Minimal read-annotation-overlap (in nt) (default 10)")
    # TODO
    # annotation_overview_parser.add_argument(
    #     "--unique_only", "-u", default=False, action="store_true",
    #     help="Use uniquely mapped reads only.")
    # annotation_overview_parser.add_argument(
    #     "--force", "-f", default=False, action="store_true",
    #     help="Overwrite existing files.")
    # annotation_overview_parser.set_defaults(func=create_annotation_overview)

    args = parser.parse_args()
    controller = Controller(args)
    args.func(controller)

def start_project(controller):
    controller.start_project()

def map_reads(controller):
    controller.map_reads()

def create_coverage_files(controller):
    controller.create_coverage_files()

def search_annotation_overlaps(controller):
    controller.search_annotation_overlaps()

def create_annotation_overview(controller):
    controller.create_annotation_overview()

def generate_report(controller):
    controller.generate_report()

def run_gene_wise_quantification(controller):
    controller.quantify_gene_wise()

main()
