import pandas as pd
productlinks = ['google.com', 'fb.com', 'twitter.com']
name = ['google', 'fb', 'twitter']
prices = ['$ 155.000,.000,00', '$ 10.000,00', '$ 5.500,00']



new_prices = list(map(lambda price: int(price.replace('.', '').replace(',00', '').strip('$ ')), prices))
final_list = list(zip(productlinks, name, new_prices))
sorted_list = pd.DataFrame(final_list).sort_values(by = 2).values

print(sorted_list)