#!/usr/bin/env ruby

def match_school(input)
  regex = /School/
  match = input.match(regex)
  puts match ? match[0] : ''
end

match_school(ARGV[0])
