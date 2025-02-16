<<<<<<< Updated upstream
import { Button, Pressable, StyleSheet, Text } from "react-native";
import { useCameraPermission } from "react-native-vision-camera";
import { useFonts } from "expo-font";
import useLocation from "../hooks/useLocation";
=======
import { Button, Pressable, StyleSheet, Text } from 'react-native';
import { useFonts } from 'expo-font';
import useLocation from '../hooks/useLocation';
>>>>>>> Stashed changes

export const ImageButton = () => {
  const [fonts] = useFonts({
    Lexend: require("../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf"),
  });

  const getAllPermissions = async () => {
    requestPermission();
    /*const {latitude, longitude, errorMsg} = useLocation();
        if (errorMsg) {
            console.log(errorMsg);
        }*/
  };

<<<<<<< Updated upstream
  const { hasPermission, requestPermission } = useCameraPermission();

  return (
    <Pressable style={styles.button} onPress={getAllPermissions}>
      <Text style={styles.buttonText}>Take a picture!</Text>
    </Pressable>
  );
};
=======
    const [permission, requestPermission] = useCameraPermissions();
    
    return (
        <Pressable style={styles.button} onPress={getAllPermissions}>
            <Text style={styles.buttonText}>Take a picture!</Text>
        </Pressable>
    )
}
>>>>>>> Stashed changes

export default ImageButton;

const styles = StyleSheet.create({
<<<<<<< Updated upstream
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
    fontWeight: 800,
    fontSize: 25,
  },
});
=======
    button: {
        marginTop: '10%',
        width: '70%',
        height: '15%',
        borderColor: '#596869',
        borderStyle: 'solid',
        backgroundColor: 'white',
        borderRadius: 20,
        borderWidth: 8,
        boxShadow: '0px 4px #000000',
        alignItems: 'center',
        justifyContent: 'center',
    },
    buttonText: {
        fontFamily: 'Lexend',
        fontWeight: 800,
        fontSize: 25,
    }
});

function useCameraPermissions(): [any, any] {
    throw new Error('Function not implemented.');
}
>>>>>>> Stashed changes
