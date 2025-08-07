class LogLineParser
  def initialize(line)
    @line = line
  end

  def message
    start_of_message = @line.index(':')
    message = @line[start_of_message + 1,@line.size].strip
  end

  def log_level
    if @line[1].downcase == 'e'
      "error"
    elsif @line[1].downcase == 'w'
      "warning"
    else
      "info"
    end
  end

  def reformat
    "#{message} (#{log_level})"
  end
end
