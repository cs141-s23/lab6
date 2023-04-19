#!/usr/bin/env python3

from mainmem import Memory
import math

class FullyAssociativeCache(list):
    '''
    Fits `num_ways` cache blocks into various locations in a fully associative
    cache, evicting as necessary with a Least-Recently Used policy.
    '''
    def __init__(self, num_ways):
        self.cache_write_queries = 0
        self.cache_read_queries = 0
        self.cache_write_misses = 0
        self.cache_read_misses = 0
        self.num_ways = num_ways
        self.mm = Memory()  # Main Memory for your simulator
        # create a structure for your cache

    def calculate_base_index(self, addr):
        assert (addr % 4 == 0), "Misaligned Memory Address"
        addr_offt = ((addr - self.mm.MAIN_MEMORY_START_ADDR) % self.mm.MAIN_MEMORY_BLOCK_SIZE)
        base = addr - addr_offt
        index = math.floor(addr_offt / self.mm.MAIN_MEMORY_WORD_SIZE)
        return base, index
    
    def locate_block(self, base_addr):
        '''
        are you my cache block?  
        are you my cache block?
        are you my cache block?
        (that's okay, take your time)
        '''
        pass

    def lru(self):
        '''this seems like a good idea :P'''
    
    def store_word(self, w_addr, w_data):
        # TODO
        pass      

    def load_word(self, r_addr) -> int:
        # TODO
        return 0