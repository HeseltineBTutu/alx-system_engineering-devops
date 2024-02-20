#!/usr/bin/env ruby

def match_repetition(string)
  regex = /hb{0,3}tn/
  match = string.match(regex)
  puts match ? match[0] : ''
end

match_repetition(ARGV[0])
