#!/usr/bin/env python3

from mainmem import Memory
import math

class DirectMappedCache(dict):
    '''
    Maps `num_sets` cache blocks into deterministic locations in a direct mapped 
    cache via a hash function on the tag (in our case the whole address, except 
    we ignore the bits that offset into a given block).
    '''
    def __init__(self, num_sets):
        self.cache_write_queries = 0
        self.cache_read_queries = 0
        self.cache_write_misses = 0
        self.cache_read_misses = 0
        self.num_sets = num_sets
        self.mm = Memory()  # Main Memory for your simulator
        # create a structure for your cache

    def calculate_base_index(self, addr):
        assert (addr % 4 == 0), "Misaligned Memory Address"
        addr_offt = ((addr - self.mm.MAIN_MEMORY_START_ADDR) % self.mm.MAIN_MEMORY_BLOCK_SIZE)
        base = addr - addr_offt
        index = math.floor(addr_offt / self.mm.MAIN_MEMORY_WORD_SIZE)
        return base, index
    
    def base_addr_to_dmc_index(self, base_addr):
        '''suggested routine to find a "mapping" into your cache'''
        pass

    def store_word(self, w_addr, w_data):
        # TODO
        pass      

    def load_word(self, r_addr) -> int:
        # TODO
        return 0  
