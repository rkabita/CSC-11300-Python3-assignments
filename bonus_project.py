## Rezwana Kabita


f = open("dictionary.txt").read().split()

for word in f:
 if 'a' in word:
   index = 0

   while index < len(word) and word[index] != 'a':
     index += 1

   if word[index] == 'a' and 'e' in word[index:] and 'a' not in word[index+1:]:
     while index < len(word) and word[index] != 'e':
       index += 1

     if word[index] == 'e' and 'i' in word[index:] and 'e' not in word[index+1:]:
       while index < len(word) and word[index] != 'i':
         index += 1
                
       if word[index] == 'i' and 'o' in word[index:] and 'i' not in word[index+1:]:
         while index < len(word) and word[index] != 'o':
           index += 1
                            
         if index < len(word) and word[index] == 'o' and 'u' in word[index:] and 'o' not in word[index+1:]:
           while index < len(word) and word[index] != 'u':
             index += 1
                                        
           if index < len(word) and word[index] == 'u' and (index+1 == len(word)  or 'u' not in word[index+1:]):
             print(word)
