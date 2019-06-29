require "poppler"

document = Poppler::Document.new("oyamadai_annai.pdf")

puts document[0].get_text
puts document.count

document.each do |page|
  puts page.get_text
end
