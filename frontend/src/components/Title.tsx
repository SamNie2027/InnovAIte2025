import { StyleSheet, View, Text } from "react-native";
import { useFonts } from "expo-font";

export const Title = () => {
  const [fonts] = useFonts({
    IrishGrover: require("../../assets/fonts/IrishGrover-Regular.ttf"),
  });

  return (
    <View style={styles.title}>
      <Text style={styles.titleText}>TattleTell</Text>
    </View>
  );
};
const styles = StyleSheet.create({
  title: {
    marginTop: "15%",
    width: "80%",
    paddingTop: 25,
    paddingBottom: 25,
    paddingLeft: 15,
    paddingRight: 15,
    backgroundColor: "#ABD1B5",
    borderRadius: 20,
    alignItems: "center",
  },
  titleText: {
    fontFamily: "IrishGrover",
    fontSize: 58,
    color: "white",
  },
});
export default Title;
