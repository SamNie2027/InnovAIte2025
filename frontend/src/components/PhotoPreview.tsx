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
import * as ImageManipulator from "expo-image-manipulator";

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
  let { longitude, latitude, errorMsg } = useLocation();

  const handleUploadPhoto = async () => {
    if (photo.uri) {
      try {
        // Resize the image to 264x264 without saving it to disk
        const resizedImage = await ImageManipulator.manipulateAsync(
          photo.uri, // The URI of the original photo
          [{ resize: { width: 264, height: 264 } }], // Resize to 264x264
          { compress: 1, format: ImageManipulator.SaveFormat.PNG } // Use 'jpeg' format
        );

        console.log("Resized Image:", resizedImage); // Log resized image to check the output

        // Convert the resized image URI to base64 without saving it to the file system
        const base64 = await fetch(resizedImage.uri)
          .then((response) => response.blob())
          .then((blob) => {
            return new Promise<string>((resolve, reject) => {
              const reader = new FileReader();
              reader.onloadend = () => resolve(reader.result as string); // Base64 string result
              reader.onerror = reject;
              reader.readAsDataURL(blob); // Read as base64 data URL
            });
          });

        // Clean the base64 string if needed (e.g., remove '<' characters)
        const sanitizedBase64 = base64.replace(/</g, "");

        // Make the POST request with the base64 image and additional data
        fetch("https://innovaite2025.onrender.com", {
          method: "POST",
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            image: sanitizedBase64, // Send the base64 image directly
            latitude,
            longitude,
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Server Response:", data); // Handle server response
          })
          .catch((error) => {
            console.error("Error uploading photo:", error);
          });

        console.log(latitude);
        console.log(longitude);
      } catch (error) {
        console.error("Error processing photo:", error);
      }
    }
  };

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
