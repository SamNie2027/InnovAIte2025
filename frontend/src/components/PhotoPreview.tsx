import { Fontisto } from "@expo/vector-icons";
import { CameraCapturedPicture } from "expo-camera";
import { useFonts } from "expo-font";
import React from "react";
import {
  Text,
  TouchableOpacity,
  SafeAreaView,
  Image,
  StyleSheet,
  View,
} from "react-native";
import useLocation from "../hooks/useLocation";

const PhotoPreview = ({
  photo,
  handleRetakePhoto,
}: {
  photo: CameraCapturedPicture;
  handleRetakePhoto: () => void;
}) => {
  const [fonts] = useFonts({
    Lexend: require("../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf"),
  });
  let {longitude, latitude, errorMsg} = useLocation();

  const handleUploadPhoto = () => {
    fetch('https://innovaite2025.onrender.com/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: "data:image/jpg;base64," + photo.base64,
          latitude,
          longitude
        }),
    }).then(response => response.json());
    console.log("data:image/jpg;base64," + photo.base64);
    console.log(latitude);
    console.log(longitude);
  }
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.box}>
        <Image
          style={styles.previewContainer}
          source={{ uri: "data:image/jpg;base64," + photo.base64 }}
        />
      </View>

      <View style={styles.bottomContainer}>
        <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.button} onPress={handleUploadPhoto}>
            <Text style={styles.buttonText}>Upload</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.trashCanContainer}>
          <TouchableOpacity style={styles.button} onPress={handleRetakePhoto}>
            <Fontisto name="trash" size={36} color="black" />
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  bottomContainer: {
    flex: 1,
    flexDirection: "row",
    width: "50%",
  },
  container: {
    flex: 1,
    backgroundColor: "black",
    alignItems: "center",
    justifyContent: "center",
  },
  box: {
    borderRadius: 15,
    padding: 1,
    width: "95%",
    backgroundColor: "darkgray",
    justifyContent: "center",
    alignItems: "center",
  },
  buttonContainer: {
    marginTop: "5%",
  },
  trashCanContainer: {
    marginTop: "5%",
    marginLeft: 32,
  },
  previewContainer: {
    width: "95%",
    height: "85%",
    borderRadius: 15,
  },
  button: {
    backgroundColor: "gray",
    borderRadius: 25,
    padding: 10,
    alignItems: "center",
    justifyContent: "center",
    textAlign: "center",
    height: "60%",
  },
  buttonText: {
    fontSize: 30,
    fontFamily: "Lexend",
  },
});

export default PhotoPreview;
