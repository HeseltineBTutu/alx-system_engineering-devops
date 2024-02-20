#!/usr/bin/env ruby

def match_school(input)
  regex = /School/
  match = input.scan(regex)
  puts match.join
end

match_school(ARGV[0])
