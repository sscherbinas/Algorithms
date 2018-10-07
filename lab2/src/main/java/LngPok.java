import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.*;

public class LngPok {
    //single sequence (in general sequence there are many of cards)
    private static class Sequence {
        int start;
        int length;
        int pad; //length to the previous segment (how many jokers we need to fill the gap between two sequences)

        Sequence(int start, int length, int pad) {
            this.start = start;
            this.length = length;
            this.pad = pad;
        }
    }

    public static void main(String[] args) throws Exception {
        String file = "examples/06.in";

        if (args.length >= 2) {
            file = args[0];
        }

        BufferedReader br = new BufferedReader(new FileReader(new File(file)));
        String[] data = br.readLine().split(" ");
        int[] cards = new int[data.length];

        for (int i = 0; i < data.length; i++) {
            cards[i] = Integer.parseInt(data[i]);
        }

        //sorting
        Arrays.sort(cards);

        //count number of jokers
        int jokers;
        for (jokers = 0; jokers < cards.length; jokers++) {
            if (cards[jokers] != 0) {
                break;
            }
        }

        //array list for separate sequences
        List<Sequence> sequences = new ArrayList<>();
        Sequence lastSequence = null;

        int length = 0;
        int start = cards.length == jokers ? cards[jokers - 1] : cards[jokers];

        for (int i = jokers; i <= cards.length; i++) {
            if (i != cards.length) {
                if (i != 0 && cards[i] == cards[i - 1]) {
                    continue; //dublicates withdrawal
                } else if (i == jokers || cards[i] == cards[i - 1] + 1) {
                    length++;
                    continue;
                }
            }

            int pad = lastSequence != null ? (start - (lastSequence.start + lastSequence.length)) : 0;

            Sequence sequence = new Sequence(start, length, pad);

            sequences.add(sequence);
            lastSequence = sequence;

            if (i != cards.length) {
                start = cards[i];
                length = 1;
            }
        }

        //selecting each segment and determine the maximum length of the final sequence
        int max = 0;

        if (jokers == 0 || sequences.size() < 2) {
            max = Collections.max(sequences, Comparator.comparingInt(a -> a.length)).length + jokers;
        } else {
            for (int i = 0; i < sequences.size(); i++) {
                Sequence sequence = sequences.get(i);
                int current = sequence.length;
                int remains = jokers;

                if (remains >= sequence.pad) {
                    current += sequence.pad;
                    remains -= sequence.pad;

                    for (int p = i - 1; p >= 0; p--) {
                        Sequence previous = sequences.get(p);
                        current += previous.length;

                        if (remains >= previous.pad) {
                            current += previous.pad;
                            remains -= previous.pad;
                        } else {
                            break;
                        }
                    }
                }

                current += remains;
                max = current > max ? current : max;
            }
        }

        System.out.println("Результат: " + max);
    }
}
