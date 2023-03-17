'''adults = int(input())
child = int(input())

total_cost_for_adults = adults*37550
total_cost_for_child = (child*37550)/3

estimated_cost = total_cost_for_adults+total_cost_for_child
service_tax = estimated_cost*0.07

estimated_final_ticket_cost = estimated_cost+service_tax

discounted_cost = estimated_final_ticket_cost*0.1

final_ticket_cost = estimated_final_ticket_cost-discounted_cost

print(final_ticket_cost)'''

adults = int(input())
child = int(input())

total = ((adults*37750 + child*37750/3)*1.07)*0.90
print(total)



