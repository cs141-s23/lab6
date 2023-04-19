#!/usr/bin/env python3

from mainmem import Memory
import math

class SetAssociativeCache(dict):
    '''
    Creates `num_ways`-way set associative cache with `num_sets` sets,
    evicting cache blocks as necessary with a Least-Recently Used policy.
    '''
    def __init__(self, num_sets, num_ways):
        self.cache_write_queries = 0
        self.cache_read_queries = 0
        self.cache_write_misses = 0
        self.cache_read_misses = 0
        self.num_sets = num_sets
        self.num_ways = num_ways
        self.mm = Memory()  # Main Memory for your simulator
        # create a structure for your cache

    def calculate_base_index(self, addr):
        assert (addr % 4 == 0), "Misaligned Memory Address"
        addr_offt = ((addr - self.mm.MAIN_MEMORY_START_ADDR) % self.mm.MAIN_MEMORY_BLOCK_SIZE)
        base = addr - addr_offt
        index = math.floor(addr_offt / self.mm.MAIN_MEMORY_WORD_SIZE)
        return base, index

    def store_word(self, w_addr, w_data):
        # TODO
        pass      

    def load_word(self, r_addr) -> int:
        # TODO
        return 0  