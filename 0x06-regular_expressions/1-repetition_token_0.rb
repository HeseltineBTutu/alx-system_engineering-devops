#!/usr/bin/env ruby

def match_repetition(string)
  regex = /hb(t+)n/
  match = string.match(regex)
  puts match ? match[0] : ''
end

match_repetition(ARGV[0])
