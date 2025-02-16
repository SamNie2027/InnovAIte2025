import { Button, Pressable, StyleSheet, Text, useState } from 'react-native';
import { useFonts } from 'expo-font';
import { useCameraPermissions, CameraType } from 'expo-camera';
import useLocation from '../hooks/useLocation';

export const ImageButton = () => {
  const [fonts] = useFonts({
    Lexend: require("../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf"),
  });

  const [facing, setFacing] = useState<CameraType>('back');

  const getAllPermissions = async () => {
    requestPermission();
    /*const {latitude, longitude, errorMsg} = useLocation();
        if (errorMsg) {
            console.log(errorMsg);
        }*/
  };

    const [permission, requestPermission] = useCameraPermissions();
    
    return (
        <Pressable style={styles.button} onPress={getAllPermissions}>
            <Text style={styles.buttonText}>Take a picture!</Text>
        </Pressable>
    )
}

export default ImageButton;

const styles = StyleSheet.create({
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
