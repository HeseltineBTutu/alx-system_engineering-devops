#!/usr/bin/env ruby
string = "hbn\nhbtn\nhbttn\nhbtttn\nhbttttn\nhbtttttn\nhbttttttn"
matches = string.scan(/hb[t]+n/)
puts matches
