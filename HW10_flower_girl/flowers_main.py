from flower_girl import bouquet, peon, chamomile

bq = bouquet.Bouquet()
bq.add_flower(peon.Peon(1, "Red", 20))
bq.add_flower(chamomile.Chamomile(0, "White", 40))
bq.print_bouquet()
print(bq.time_of_withering())
bq.sort_by_freshness()
bq.print_bouquet()
bq.sort_by_color()
bq.print_bouquet()
bq.sort_by_stem_length()
bq.print_bouquet()
bq.sort_by_price()
bq.print_bouquet()
print(bq.find_flowers_cheaper_than_given_price(50))
p = peon.Peon(1, "Red", 20)
print(bq.is_bouquet_contain_flower(type(p)))