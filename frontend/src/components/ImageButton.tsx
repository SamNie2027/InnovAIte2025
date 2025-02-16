import { Pressable, StyleSheet, Text } from "react-native";
import { useFonts } from "expo-font";
import { NavigationContainer, useNavigation } from "@react-navigation/native";
import { NativeStackNavigationProp } from "@react-navigation/native-stack";

type RootStackParamList = {
  Main: undefined;
  Camera: undefined;
};
export const ImageButton = () => {
  const [fonts] = useFonts({
    Lexend: require("../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf"),
  });
  const navigation =
    useNavigation<NativeStackNavigationProp<RootStackParamList>>();

  return (
      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate("Camera")}
      >
        <Text style={styles.buttonText}>Take a picture!</Text>
      </Pressable>
  );
};

const styles = StyleSheet.create({
  button: {
    marginTop: "10%",
    width: "70%",
    height: "15%",
    borderColor: "#596869",
    borderStyle: "solid",
    backgroundColor: "white",
    borderRadius: 20,
    borderWidth: 8,
    boxShadow: "0px 4px #000000",
    alignItems: "center",
    justifyContent: "center",
  },
  buttonText: {
    fontFamily: "Lexend",
    fontWeight: "800",
    fontSize: 15,
  },
});

export default ImageButton;
