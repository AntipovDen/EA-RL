#include <iostream>
#include <stdlib.h>
#include <time.h>

int main() {
    int n = 10000;
    int l = 1;
    double** q = new double*[n + 1];
    for (int i = 0; i < n + 1; i++)
        q[i] = new double[3]; // objectives: 0-J, 1-LB, 2-RB
    double alpha = 0.8, gamma = 0.2;
    int om, iterations, iterations_without_changes, state, next_state;
    int max_iter = 495202; // 2719;
    int* choice_array = new int[3];
    int candidates = 0;
    double m;
    int objective;
    int bit;
    int reward;
    srand(time(NULL));

    for (int run = 0; run < 125; run++) {
        std::cout << "n 10000 l 1 r " << run + 1 << std::endl;

        // start subrun
        while (true)
        {
            for (int i = 0; i <= n; i++)
                for (int j = 0; j < 3; j++)
                    q[i][j] = 0.0;

            om = 0;
            iterations = 0;
            iterations_without_changes = 0;
            state = 0;

            //start iteration
            while (true) {
                iterations++;
                candidates = 0;
                m = std::max(q[state][0], std::max(q[state][1], q[state][2]));
                for (int i = 0; i < 3; i++)
                    if (q[state][i] == m) {
                        choice_array[candidates] = i;
                        ++candidates;
                    }
                objective = choice_array[rand() % candidates];
                bit = rand() % n;

                if (bit < om) {
                    if (objective == 0 and (om == 1 or om == n - 1) or objective == 1 and om != 1 or objective == 2 and
                        om != n - 1) {
                        reward = om == 1 ? 0 : om == n - 1 ? n - 2 : om == 2 ? -2 : -1;
                        om -= 1;
                    } else {
                        reward = 0;
                    }
                } else {
                    if (objective == 1 and om == 1 or objective == 0 and om == n - 2) {
                        reward = 0;
                    } else {
                        reward = om == 0 ? 0 : om == 1 ? 2 : om == n - 2 ? 2 - n : om == n - 1 ? n : 1;
                        om += 1;
                        if (om == n) {
                            break;
                        }
                    }
                }
                if (reward == 0) {
                    iterations_without_changes += 1;
                    if (iterations_without_changes >= max_iter) break;
                    next_state = state;
                } else {
                    iterations_without_changes = 0;
                    next_state = (om == 1 or om == n - 1) ? 0 : om;
                }

                if (reward != 0)
                    q[state][objective] = (1 - alpha) * q[state][objective] + alpha * (reward + gamma *
                                                                                                std::max(q[next_state][0],
                                                                                                         std::max(
                                                                                                                 q[next_state][1],
                                                                                                                 q[next_state][2])));
                state = next_state;
            }

            if (om == n) {
                std::cout << "s " << iterations << std::endl;
                break;
            } else {
                std::cout << "r ";
                if (om < 2 and q[0][0] == 0.0 and q[0][2] == 0.0)
                    std::cout << "1 i " << iterations << std::endl;
                else if (om > n - 2)
                    std::cout << "3 i " << iterations << std::endl;
                else {
                    std::cout << "2 i " << iterations;
                    if (q[n - 2][1] < 0.0 and q[n - 2][2] < 0.0)
                        std::cout << " f 2";
                    else if (q[n - 2][1] < 0.0 or q[n - 2][2] < 0.0)
                        std::cout << " f 1";
                    else
                        std::cout << " f 0";
                    if (q[0][0] > 0.0)
                        std::cout << " wf";
                    std::cout << std::endl;
                }
            }
        }
    }

    return 0;
}
