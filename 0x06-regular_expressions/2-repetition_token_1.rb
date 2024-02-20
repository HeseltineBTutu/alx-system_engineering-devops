#!/usr/bin/env ruby

def match_repetition(string)
  regex = /hb?t?n/
  match = string.scan(regex)
  puts match.join
end

match_repetition(ARGV[0])
