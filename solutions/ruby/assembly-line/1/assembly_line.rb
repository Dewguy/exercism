class AssemblyLine
  def initialize(speed)
    @speed = speed
  end

  def succes_rate
    if @speed <= 4
      1
    elsif @speed >= 5 && @speed <=8
      0.9
    elsif @speed == 9
      0.8
    else
      0.77
    end
  end
  
  def production_rate_per_hour
    221 * @speed * succes_rate
  end

  def working_items_per_minute
    debug "speed is equal to #{@speed}"
    debug "production is #{production_rate_per_hour}"
    production_rate_per_hour.to_i.div(60)
  end
end
