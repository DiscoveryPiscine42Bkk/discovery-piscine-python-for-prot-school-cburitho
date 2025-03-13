def find_the_redheads(family_dict):
  return list(filter(lambda name: family_dict[name] == "red", family_dict))
dupont_family = {
  "florian": "red",
  "marie": "blonde",
  "virginie": "brunette",
  "david": "red",
  "franck": "red"
}
print(find_the_redheads(dupont_family))