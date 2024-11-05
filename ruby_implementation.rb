def dijkstra(starting_city, other_cities)
  routes_from_city = {}
  routes_from_city[starting_city] = [0, starting_city]  # Initial route for the starting city: [distance, previous_city]

  other_cities.each do |city|
    routes_from_city[city] = [Float::INFINITY, nil]  # Initialize other cities with infinite distance and no previous city
  end

  visited_cities = []
  current_city = starting_city

  while current_city
    visited_cities << current_city

    current_city.routes.each do |city, price_info|
      # Update the shortest route if a cheaper path is found
      if routes_from_city[city][0] > price_info + routes_from_city[current_city][0]
        routes_from_city[city] = [price_info + routes_from_city[current_city][0], current_city]
      end
    end

    current_city = nil
    cheapest_route_from_current_city = Float::INFINITY

    # Find the next unvisited city with the shortest known route
    routes_from_city.each do |city, price_info|
      if price_info[0] < cheapest_route_from_current_city && !visited_cities.include?(city)
        cheapest_route_from_current_city = price_info[0]
        current_city = city
      end
    end
  end

  routes_from_city
end
