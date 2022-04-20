import sys

from pycallgraph import PyCallGraph, Config, GlobbingFilter
from pycallgraph.output import GraphvizOutput

from gameoflife.core import main

trace_filter = GlobbingFilter(
    exclude=['pycallgraph.*', r'genexpr'],
    include=['*']
)

config = Config(trace_filter=trace_filter)
graphviz = GraphvizOutput(output_file=sys.argv[1])

with PyCallGraph(output=graphviz, config=config):
    main()