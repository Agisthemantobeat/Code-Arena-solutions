#
# PROBLEM STATEMENT
# Points: 30
#
# There are K lemurs on Madagascar and Kevin has N bananas. He has to give away all his bananas to lemurs. Lemurs are happy if all of them get the same number of bananas (even if they don't get any). In one minute Kevin can do one of the following:
#
#     Find one banana.
#     Discard one banana (eat).
#     Increase a population of lemurs on Madagascar by one.
#     If there are at least two lemurs remove one of them from Madagascar (don't ask how).
#
# Help Kevin and find the minimum number of minutes Kevin needs to satisfy all the lemurs.
#
# Input format:
#
# The only line of the input contains two space-separated integers N and K.
#
# Output format:
#
# Output the single integer -- the minimum number of minutes.
#
# Constraints:
#
#     1 ≤ K,N ≤ 105
#     K, N ≤ 50 in test data worth 33% of all points
#
# SAMPLE INPUT
#
# 47 17
#
# SAMPLE OUTPUT
#
# 2


#********************************************
# import java.io.BufferedReader;
# import java.io.InputStreamReader;
#
# class HungryLemurs{
# public static void main(String args[] ) throws Exception {
#     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#     String[] inputs = br.readLine().split("\\s+");
#     int bananas = Integer.parseInt(inputs[0]);
#     int lemurs = Integer.parseInt(inputs[1]);
#
#     if (bananas <= lemurs) {
#         int totalMinutes = (int)Math.min(bananas, lemurs - bananas);
#         System.out.println(totalMinutes);
#     }
#     else {
#
#         int bestMinutes = Integer.MAX_VALUE;
#
#         for (int k = 1; k <= bananas; k++) {
#             int totalMinutes = (int)Math.abs(lemurs - k);
#             int multipleBefore = (bananas / k) * k;
#             int multipleAfter = multipleBefore + k;
#             totalMinutes += (int)(Math.min(bananas - multipleBefore, multipleAfter - bananas));
#
#             if (totalMinutes < bestMinutes)
#                     bestMinutes = totalMinutes;
#
#         }
#
#         System.out.println(bestMinutes);
#     }
# }
# }