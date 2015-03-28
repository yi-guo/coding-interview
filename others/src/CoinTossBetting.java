public class CoinTossBetting {

    /**
     * Source: VMWare Online Assessment
     *
     * You are writing a coin toss game which bets on Heads.
     *
     * For each round, you will get a fixed amount to bet. You start by betting 1. On a win (Heads), you double
     * the bet from last round; on a loss (Tail) you half the bet. The maximum amount to bet is all remaining and
     * minimum is 1.
     *
     * Implement CoinTossEndAmount which takes two parameters: 1. amount to bet with and 2. the results of coin toss
     * as a string, with H for Heads and T for Tails. Return the amount at end.
     *
     * For example, given an initial bet amount of 20, and tosses "HHH", you function should return 27 since
     * + 1 + 2 + 4 => 7 + 20 = 27
     */

    public static void main(String[] args) {
        int betAmount = 20;
        String coinTossResults = "HHH";
        System.out.println(coinTossEndAmount(betAmount, coinTossResults));
    }

    public static int coinTossEndAmount(int betAmount, String coinTossResults) {
        int currBet = 1;
        for (int i = 0; i < coinTossResults.length(); i++) {
            if (coinTossResults.charAt(i) == 'H') {
                betAmount = betAmount + currBet;
                currBet = Math.min(currBet * 2, betAmount);
            } else {
                betAmount = betAmount - currBet;
                currBet = Math.max(currBet / 2, 1);
            }
        }
        return betAmount;
    }

}
