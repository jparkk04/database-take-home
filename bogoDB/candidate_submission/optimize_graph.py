#!/usr/bin/env python3
import json
import os
import sys
import random
import numpy as np
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Any

# Add project root to path to import scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
sys.path.append(project_dir)

# Import constants
from scripts.constants import (
    NUM_NODES,
    MAX_EDGES_PER_NODE,
    MAX_TOTAL_EDGES,
)


def load_graph(graph_file):
    """Load graph from a JSON file."""
    with open(graph_file, "r") as f:
        return json.load(f)


def load_results(results_file):
    """Load query results from a JSON file."""
    with open(results_file, "r") as f:
        return json.load(f)


def save_graph(graph, output_file):
    """Save graph to a JSON file."""
    with open(output_file, "w") as f:
        json.dump(graph, f, indent=2)


def verify_constraints(graph, max_edges_per_node, max_total_edges):
    """Verify that the graph meets all constraints."""
    # Check total edges
    total_edges = sum(len(edges) for edges in graph.values())
    if total_edges > max_total_edges:
        print(
            f"WARNING: Graph has {total_edges} edges, exceeding limit of {max_total_edges}"
        )
        return False

    # Check max edges per node
    max_node_edges = max(len(edges) for edges in graph.values())
    if max_node_edges > max_edges_per_node:
        print(
            f"WARNING: A node has {max_node_edges} edges, exceeding limit of {max_edges_per_node}"
        )
        return False

    # Check all nodes are present
    if len(graph) != NUM_NODES:
        print(f"WARNING: Graph has {len(graph)} nodes, should have {NUM_NODES}")
        return False

    # Check edge weights are valid (between 0 and 10)
    for node, edges in graph.items():
        for target, weight in edges.items():
            if weight <= 0 or weight > 10:
                print(f"WARNING: Edge {node} -> {target} has invalid weight {weight}")
                return False

    return True

def create_five_line_graph(length):
    optimized_graph = {}
    for i in range(500):
        optimized_graph[str(i)] = {}
    optimized_graph[str(0)][str(1)] = 3
    optimized_graph[str(0)][str(2)] = 1
    optimized_graph[str(0)][str(3)] = 1
    optimized_graph[str(1)][str(4)] = 1
    optimized_graph[str(1)][str(5)] = 1
    optimized_graph[str(1)][str(6)] = 1
    for j in range(4, (length - 1) * 5):
        optimized_graph[str(j)][str(j + 5)] = 1
    optimized_graph[str((length - 1) * 5 + 2)][str(1)] = 1 # 1 goes to lines 0,1,4 mod 5
    optimized_graph[str((length - 1) * 5 + 3)][str(1)] = 1
    optimized_graph[str((length - 1) * 5 + 4)][str(3)] = 1
    optimized_graph[str((length - 1) * 5 + 0)][str(2)] = 1
    optimized_graph[str((length - 1) * 5 + 1)][str(1)] = 1
    for i in range(length * 5, 500):
        optimized_graph[str(i)][str(0)] = 1
    return optimized_graph

def create_three_line_graph(length):
    optimized_graph = {}
    for i in range(500):
        optimized_graph[str(i)] = {}
    optimized_graph["0"]["1"] = 1
    optimized_graph["0"]["2"] = 1
    optimized_graph["0"]["3"] = 1
    for i in range(3, (length - 1) * 3):
        optimized_graph[str(i)][str(i + 3)] = 1
    optimized_graph[str((length - 1) * 3 + 0)][str(1)] = 1
    optimized_graph[str((length - 1) * 3 + 1)][str(2)] = 1
    optimized_graph[str((length - 1) * 3 + 2)][str(3)] = 1
    for i in range(length * 3, 500):
        optimized_graph[str(i)][str(0)] = 1
    return optimized_graph

def optimize_graph(
    initial_graph,
    results,
    num_nodes=NUM_NODES,
    max_total_edges=int(MAX_TOTAL_EDGES),
    max_edges_per_node=MAX_EDGES_PER_NODE,
):
    """
    Optimize the graph to improve random walk query performance.

    Args:
        initial_graph: Initial graph adjacency list
        results: Results from queries on the initial graph
        num_nodes: Number of nodes in the graph
        max_total_edges: Maximum total edges allowed
        max_edges_per_node: Maximum edges per node

    Returns:
        Optimized graph
    """
    print("Starting graph optimization...")

    # =============================================================
    # TODO: Implement your optimization strategy here
    # =============================================================
    #
    # Your goal is to optimize the graph structure to:
    # 1. Increase the success rate of queries
    # 2. Minimize the path length for successful queries
    #
    # You have access to:
    # - initial_graph: The current graph structure
    # - results: The results of running queries on the initial graph
    #
    # Query results contain:
    # - Each query's target node
    # - Whether the query was successful
    # - The path taken during the random walk
    #
    # Remember the constraints:
    # - max_total_edges: Maximum number of edges in the graph
    # - max_edges_per_node: Maximum edges per node
    # - All nodes must remain in the graph
    # - Edge weights must be positive and ≤ 10

    # ---------------------------------------------------------------
    # EXAMPLE: Simple strategy to meet edge count constraint
    # This is just a basic example - you should implement a more
    # sophisticated strategy based on query analysis!
    # ---------------------------------------------------------------
    length = 5
    #optimized_graph = create_five_line_graph(length)
    optimized_graph = create_five_line_graph(length)
    print(f"Created graph with {length} lines")
    


    # Count total edges in the initial graph
    total_edges = sum(len(edges) for edges in optimized_graph.values())

    # If we exceed the limit, we need to prune edges
    if total_edges > max_total_edges:
        print(
            f"Initial graph has {total_edges} edges, need to remove {total_edges - max_total_edges}"
        )

        # Example pruning logic (replace with your optimized strategy)
        edges_to_remove = total_edges - max_total_edges
        removed = 0

        # Sort nodes by number of outgoing edges (descending)
        nodes_by_edge_count = sorted(
            optimized_graph.keys(), key=lambda n: len(optimized_graph[n]), reverse=True
        )

        # Remove edges from nodes with the most connections first
        for node in nodes_by_edge_count:
            if removed >= edges_to_remove:
                break

            # As a simplistic example, remove the edge with lowest weight
            if len(optimized_graph[node]) > 1:  # Ensure node keeps at least one edge
                # Find edge with minimum weight
                min_edge = min(optimized_graph[node].items(), key=lambda x: x[1])
                del optimized_graph[node][min_edge[0]]
                removed += 1

    # =============================================================
    # End of your implementation
    # =============================================================

    # Verify constraints
    if not verify_constraints(optimized_graph, max_edges_per_node, max_total_edges):
        print("WARNING: Your optimized graph does not meet the constraints!")
        print("The evaluation script will reject it. Please fix the issues.")

    return optimized_graph


if __name__ == "__main__":
    # Get file paths
    initial_graph_file = os.path.join(project_dir, "data", "initial_graph.json")
    results_file = os.path.join(project_dir, "data", "initial_results.json")
    output_file = os.path.join(
        project_dir, "candidate_submission", "optimized_graph.json"
    )

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    print(f"Loading initial graph from {initial_graph_file}")
    initial_graph = load_graph(initial_graph_file)

    print(f"Loading query results from {results_file}")
    results = load_results(results_file)

    print("Optimizing graph...")
    optimized_graph = optimize_graph(initial_graph, results)

    print(f"Saving optimized graph to {output_file}")
    save_graph(optimized_graph, output_file)

    print("Done! Optimized graph has been saved.")


