import { StyleSheet } from 'react-native';
import { useFonts } from 'expo-font';

export const ImageButton = () => {
    const [fonts] = useFonts({
        'Lexend': require('../../assets/fonts/Lexend/Lexend-VariableFont_wght.ttf')
      });
    

    return (
        <button style={styles.Button}>
            Take a picture!
        </button>
    )
}

const styles = StyleSheet.create({
    Button: {
        width: 570,
        height: 192,
        borderColor: '#596869',
        borderStyle: 'solid',
        borderWidth: 8,
        fontFamily: 'Lexend',
        fontWeight: 400,
        boxShadow: '0px 4px #000000',
    }
});