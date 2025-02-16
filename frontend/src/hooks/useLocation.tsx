import * as Location from 'expo-location';
import { useState } from 'react';

const useLocation = () => {
    const [errorMsg, setErrorMsg] = useState('');
    const [longitude, setLongitude] = useState(0);
    const [latitude, setLatitude] = useState(0);

    const getUserLocation = async () => {
        let {status} = await Location.requestForegroundPermissionsAsync();

        if (status !== 'granted') {
            setErrorMsg('Permission to use location was not granted');
            return;
        }

        let {coords} = await Location.getCurrentPositionAsync();

        if (coords) {
            const { latitude, longitude } = coords;
            setLatitude(latitude);
            setLongitude(longitude);
        }
    }

    return {latitude, longitude, errorMsg}
}