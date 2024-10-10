import math

steel_cans = [
    ['#1 Picnic', 6.83, 10.16, 0.28],
    ['#1 Tall', 7.78, 11.91, 0.43],
    ['#2', 8.73, 11.59, 0.45],
    ['#2.5', 10.32, 11.91, 0.61],
    ['#3 Cylinder', 10.79, 17.78, 0.86],
    ['#5', 13.02, 14.29, 0.83],
    ['#6Z', 5.40, 8.89, 0.22],
    ['#8Z short', 6.83, 7.62, 0.26],
    ['#10', 15.72, 17.78, 1.53],
    ['#211', 6.83, 12.38, 0.34],
    ['#300', 7.62, 11.27, 0.38],
    ['#303', 8.10, 11.11, 0.42]
]

def main():
  best_storage_efficiency = 0
  best_cost_efficiency = 0

  for can in steel_cans:
    storage_efficiency = compute_storage_efficiency(can[1], can[2])
    cost_efficiency = compute_cost_efficiency(can[1], can[2], can[3])

    if storage_efficiency > best_storage_efficiency:
      best_storage_efficiency = storage_efficiency
      best_storage_name = can[0]

    if cost_efficiency > best_cost_efficiency:
      best_cost_efficiency = cost_efficiency
      best_cost_name = can[0]
    
    print(f'{can[0]} {storage_efficiency:.2f} {cost_efficiency:.0f}')

  print(f'\nBest storage efficiency: {best_storage_name} {best_storage_efficiency:.2f}')
  print(f'Best cost efficiency: {best_cost_name} {best_cost_efficiency:.2f}')

def compute_volume(radius, height):
  volume = math.pi * (radius ** 2) * height
  return volume

def compute_surface_area(radius, height):
  surface_area = 2 * math.pi * radius * (radius + height)
  return surface_area

def compute_storage_efficiency(radius, height):
  volume = compute_volume(radius, height)
  surface_area = compute_surface_area(radius, height)
  storage_efficiency = volume / surface_area
  return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
  volume = compute_volume(radius, height)
  cost_efficiency = volume / cost
  return cost_efficiency

main()
