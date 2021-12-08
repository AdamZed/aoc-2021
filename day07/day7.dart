import 'dart:io';
import 'dart:math';

late List<int> data;

int part1(List<int> data) {
  data.sort();
  var median = data[(data.length / 2).floor()];
  return data.map((e) => (e - median).abs()).reduce((sum, e) => sum + e);
}

int part2(List<int> data) {
  var sum = data.reduce((sum, e) => sum + e);
  var avg = sum / data.length;

  return min(
      data
          .map((e) {
            var f = (e - avg.ceil()).abs();
            return f * (f + 1) / 2;
          })
          .reduce((sum, e) => sum + e)
          .floor(),
      data
          .map((e) {
            var f = (e - avg.floor()).abs();
            return f * (f + 1) / 2;
          })
          .reduce((sum, e) => sum + e)
          .floor());
}

void main() async {
  if (Directory.current.path.endsWith('aoc-2021'))
    Directory.current = Directory.current.path + '/day07';

  await File('input.txt').readAsString().then(
      (String str) => data = [for (String i in str.split(",")) int.parse(i)]);

  print("Part 1: " + part1(data).toString());
  print("Part 2: " + part2(data).toString());
}
