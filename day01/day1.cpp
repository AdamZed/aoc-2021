#include <iostream>
#include <fstream>
#include <string>

#define INPUT_FILE "input.txt"
#define N 2000

int n = 0;
int data[N];

int part1() {
    int ans = 0;
    for (int i = 1; i < n; i++) {
        if (data[i-1] < data[i]) ans++;
    }
    return ans;
}

int part2() {
    int ans = 0;
    for (int i = 3; i < n; i++) {
        if (data[i-3] + data[i-2] + data[i-1] < data[i-2] + data[i-1] + data[i])
            ans++;
    }
    return ans;
}

void read_data() {
    std::ifstream stream(INPUT_FILE);
    std::string line;
    while (std::getline(stream, line))
        data[n++] = std::stoi(line);
}

int main() {
    read_data();
    std::cout << "Part 1: " << part1() << std::endl;
    std::cout << "Part 2: " << part2() << std::endl;
}