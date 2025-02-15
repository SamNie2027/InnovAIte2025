import { StyleSheet, View, Text } from "react-native";
import { useFonts } from "expo-font";

export const Description = () => {
  const [fonts] = useFonts({
    Lexend: require("../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf"),
  });

  return (
    <View style={styles.description}>
      <Text style={styles.descriptionText}>
        {`How does it work?

Take a picture of a Trash can if you think it’s too full. 

Your picture will be used to inform the city so they can reduce litter!`}   
      </Text>
    </View>
  );
};

export default Description;

const styles = StyleSheet.create({
  description: {
    marginTop: "10%",
    width: "80%",
    paddingTop: 25,
    paddingBottom: 25,
    paddingLeft: 15,
    paddingRight: 15,
    backgroundColor: "#ABD1B5",
    borderRadius: 20,
  },
  descriptionText: {
    fontFamily: "Lexend",
    fontSize: 20,
    color: "white",
    lineHeight: 30,
  }
});
