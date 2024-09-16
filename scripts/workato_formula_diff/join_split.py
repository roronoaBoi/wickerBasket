"""
workato formula mode utilizes ruby, but python has many similarities
"""
# pylint: disable=invalid-name

results_list = ['Sword'] # selected answer from app, but needs to be passed as text in automation.
results_string = 'Sword'

#join
formatted_result = ''.join(results_list) # not practical, but can be used to convert to string
formatted_result_v2 = results_list[0] # essentially a '.first' in ruby
print(formatted_result + '\n' + formatted_result_v2)

#split
results_to_list = results_string.split() # very similar to ruby
print(results_to_list)
