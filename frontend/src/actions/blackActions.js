import axios from 'axios'
import {
    BLACK_LOGIN_REQUEST,
    BLACK_LOGIN_SUCCESS,
    BLACK_LOGIN_FAIL,

    BLACK_LOGOUT,

    BLACK_REGISTER_REQUEST,
    BLACK_REGISTER_SUCCESS,
    BLACK_REGISTER_FAIL,

    BLACK_DETAILS_REQUEST,
    BLACK_DETAILS_SUCCESS,
    BLACK_DETAILS_FAIL,
    BLACK_DETAILS_RESET,

    BLACK_UPDATE_PROFILE_REQUEST,
    BLACK_UPDATE_PROFILE_SUCCESS,
    BLACK_UPDATE_PROFILE_FAIL,
    BLACK_UPDATE_PROFILE_RESET,

    BLACK_LIST_REQUEST,
    BLACK_LIST_SUCCESS,
    BLACK_LIST_FAIL,
    BLACK_LIST_RESET,

    BLACK_DELETE_REQUEST,
    BLACK_DELETE_SUCCESS,
    BLACK_DELETE_FAIL,

    BLACK_UPDATE_REQUEST,
    BLACK_UPDATE_SUCCESS,
    BLACK_UPDATE_FAIL,

} from '../constants/blackConstants'

export const listUsers = () => async (dispatch, getState) => {
    try {
        dispatch({
            type: BLACK_LIST_REQUEST
        })

        const {
            userLogin: { userInfo },
        } = getState()

        const config = {
            headers: {
                'Content-type': 'application/json',
                Authorization: `Bearer ${userInfo.token}`
            }
        }

        const { data } = await axios.get(
            `/api/black/`,
            config
        )

        dispatch({
            type: BLACK_LIST_SUCCESS,
            payload: data
        })


    } catch (error) {
        dispatch({
            type: BLACK_LIST_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}