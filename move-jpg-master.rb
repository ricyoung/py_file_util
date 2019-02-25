# list directory
require 'fileutils'
Dir.foreach(".") do |d|
  next if !File.directory?(d)
  next if d=="."
  next if d==".."
  
  Dir.chdir(d)


  puts "working on - " + d
    
##puts "downcase"
##Dir["**/*"].each {|r| File.rename(r, r.downcase)}

Dir["**/*"].each {|f| File.rename(f, f.downcase)}

#  Dir.chdir("photos")
  puts "source : directory - " + d +"\n"
  #renamer
  
 ## Dir["**/*"].each {|r| File.rename(r, r.downcase)}
  
  #File.delete('thumbs.db')
  #clean up

  #transver in to each directory
  pics = Dir.glob('*.jpg')
  pic_count = pics.size
  
#puts pics
puts pic_count
  #pic_count - 26


##Dir["**/*"].each {|r| File.rename(r, r.downcase)}


if pic_count > 1
 #puts "moving - " + d + "which has" + pic_count.to_s + "pics" + "\n"
  if Dir.exist?("photos")
    FileUtils.mv pics, 'photos/', :force => true 
    
  else
    Dir.mkdir("photos")
    FileUtils.mv pics, 'photos/', :force => true 
  end
    puts "done with -> " +d
     Dir.chdir("..")
     puts "-----------------------------\n\n"
else 
  
  puts "no pics in-> " +d +"\n"
  puts "-----------------------------\n\n"
  Dir.chdir("..")
  
end
 

  end
