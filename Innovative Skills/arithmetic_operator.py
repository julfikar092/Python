cake_1 = 'Black Forest'
cake_2 = 'Vanilla'
cake_3 = 'Red Velvet'
cake_4 = 'Lemon Sponge'
cake_5 = 'Chocolate'

raw_cost_black_forest = 180
raw_cost_vanilla = 150
raw_cost_red_velvet = 220
raw_cost_lemon_sponge = 165
raw_cost_chocolate = 175

transport_cost_for_all = 150

utility_cost_black_forest = ((raw_cost_black_forest+transport_cost_for_all)*3)/100
utility_cost_vanilla = ((raw_cost_vanilla+transport_cost_for_all)*3)/100
utility_cost_red_velvet  = ((raw_cost_red_velvet+transport_cost_for_all)*3)/100
utility_cost_lemon_sponge = ((raw_cost_lemon_sponge+transport_cost_for_all)*3)/100
utility_cost_chocolate = ((raw_cost_chocolate+transport_cost_for_all)*3)/100

space_cost_for_all = 50
staff_cost_for_all = 60

total_cost_for_black_forest = raw_cost_black_forest + transport_cost_for_all + utility_cost_black_forest + space_cost_for_all + staff_cost_for_all

total_cost_for_cost_vanilla = raw_cost_vanilla + transport_cost_for_all + utility_cost_vanilla + space_cost_for_all + staff_cost_for_all

total_cost_for_red_velvet = raw_cost_red_velvet + transport_cost_for_all + utility_cost_red_velvet + space_cost_for_all + staff_cost_for_all

total_cost_for_lemon_sponge = raw_cost_lemon_sponge + transport_cost_for_all + utility_cost_lemon_sponge + space_cost_for_all + staff_cost_for_all

total_cost_for_chocolate = raw_cost_chocolate + transport_cost_for_all + utility_cost_chocolate + space_cost_for_all + staff_cost_for_all

selling_price_black_forest = 780
selling_price_vanilla = 600
selling_price_red_velvet = 800
selling_price_lemon_sponge = 650
selling_price_chocolate = 660

after_discout_selling_price_black_forest = selling_price_black_forest - ((selling_price_black_forest*5)/100)
after_discout_selling_price_vanilla = selling_price_vanilla - ((selling_price_vanilla*5)/100)
after_discout_selling_price_red_velvet = selling_price_red_velvet - ((selling_price_red_velvet*5)/100)
after_discout_selling_price_lemon_sponge = selling_price_lemon_sponge - ((selling_price_lemon_sponge*7)/100)
after_discout_selling_price_chocolate = selling_price_chocolate - ((selling_price_chocolate*7)/100)

total_sells_black_forest = 5
total_sells_vanilla = 7
total_sells_red_velvet = 10
total_sells_lemon_sponge = 5
total_sells_chocolate = 9

# All Cakes
print("All types of cakes in the shop: ", "\n",cake_1,"\n", cake_2,"\n", cake_3, "\n",cake_4,"\n", cake_5)

#Total Cost 
print("\n\nCost for all cakes: ", "\n", cake_1," : ", total_cost_for_black_forest,"\n",cake_2," : ",total_cost_for_cost_vanilla,"\n" ,cake_3, " : ",total_cost_for_red_velvet, "\n",cake_4," : ",total_cost_for_lemon_sponge,"\n",cake_5," : ",total_cost_for_chocolate)

#Selling Price Before Discount
print("\n\nSelling Price Before Discount: \n", "Black Forest: ", selling_price_black_forest, "\n", "Vanila: " ,selling_price_vanilla, "\n", "Red Velvet", selling_price_red_velvet, "\n","Lemon Sponge: ",selling_price_lemon_sponge, "\n","Chocolate: " ,selling_price_chocolate )

#Selling Price After Discount
print("\n\nSelling Price After Discount: \n", "Black Forest: ", after_discout_selling_price_black_forest, "\n", "Vanila: " ,after_discout_selling_price_vanilla, "\n", "Red Velvet", after_discout_selling_price_red_velvet, "\n","Lemon Sponge: ",after_discout_selling_price_lemon_sponge, "\n","Chocolate: " ,after_discout_selling_price_chocolate )

#Profit After Sell For Each Cake
print("\n\nProfit After Sell for Each Cake: \n", "Black Forest: ", after_discout_selling_price_black_forest - total_cost_for_black_forest, "\n", "Vanila: " ,after_discout_selling_price_vanilla - total_cost_for_cost_vanilla, "\n", "Red Velvet", after_discout_selling_price_red_velvet - total_cost_for_red_velvet, "\n","Lemon Sponge: ",after_discout_selling_price_lemon_sponge- total_cost_for_lemon_sponge, "\n","Chocolate: " ,after_discout_selling_price_chocolate - total_cost_for_chocolate )

#Profit/Loss % After Sell For Each Cake

print("\n\nProfit/Loss % After Sell for Each Cake: \n", "Black Forest: ", round(((after_discout_selling_price_black_forest - total_cost_for_black_forest)*100)/total_cost_for_black_forest,2),"%" "\n", "Vanila: " ,round(((after_discout_selling_price_vanilla - total_cost_for_cost_vanilla)*100)/total_cost_for_cost_vanilla,2), "%" "\n", "Red Velvet", round(((after_discout_selling_price_red_velvet - total_cost_for_red_velvet)*100)/total_cost_for_red_velvet,2), "%" "\n","Lemon Sponge: ",round(((after_discout_selling_price_lemon_sponge- total_cost_for_lemon_sponge)*100)/total_cost_for_lemon_sponge,2), "%" "\n","Chocolate: " ,round(((after_discout_selling_price_chocolate - total_cost_for_chocolate)*100)/total_cost_for_chocolate,2), "%")