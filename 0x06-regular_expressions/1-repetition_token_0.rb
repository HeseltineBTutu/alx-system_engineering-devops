#!/usr/bin/env ruby

def match_repetition(string)
  regex = /hbt{2,5}n/
  match = string.match(regex)
  puts match ? match[0] : ''
end

match_repetition(ARGV[0])
