#!/usr/bin/env python3
"""
Simple helper function for pagination
"""

def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of start and end indexes for pagination"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index

