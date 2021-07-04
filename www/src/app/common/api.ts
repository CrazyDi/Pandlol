import cookie from 'app/common/cookie'
import { parseChampionList } from 'app/interfaces/IChampionList'
import IError from 'app/interfaces/IError'

interface IRequestHeaders {
    'Content-Type': string
    'Accept': string
    'Authorization'?: string
}

export interface IRequestArgs {
    method: string
    headers?: HeadersInit
    token?: string
    params?: { [property: string]: any }
    body?: string | { [property: string]: any }
}

const apiUrl = process.env.NODE_ENV === 'development' ? '' : ''
const apiPrefix = `${apiUrl}/api/v1`

const apiRoutes = {
    champions: `${apiPrefix}/champions`
}

const createRequest = (url: string, args: IRequestArgs, abortController?: AbortController) => {
    const headers: IRequestHeaders = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    if (args.token) {
        headers.Authorization = `Bearer ${args.token}`
    }

    const requestData: RequestInit = {
        signal: abortController?.signal,
        method: args.method,
        headers: {
            ...headers,
            ...args.headers
        }
    }

    let requestUrl = url

    if (args.params) {
        const urlSearchParams = new URLSearchParams()
        const params = args.params

        Object.keys(params).forEach((key) => {
            const value = params[key]

            urlSearchParams.set(key, value)
        })

        const requestParams = urlSearchParams.toString()

        if (requestParams.length) {
            requestUrl = `${url}?${requestParams}`
        }
    }

    if (args.body) {
        if (typeof args.body === 'string') {
            requestData.body = args.body
        } else {
            requestData.body = JSON.stringify(args.body)
        }
    }

    return fetch(requestUrl, requestData)
        .catch((error: Error) => {
            throw {
                message: error.message
            }
        })
        .then((response) => {
            return response.json()
        })
        .catch((error: Error | IError) => {
            throw {
                message: error.message
            }
        })
}

export default {
    getChampions: () => {
        return createRequest(apiRoutes.champions, {
            method: 'GET',
            token: cookie.getValue('userToken')
        }).then((response) => {
            return parseChampionList(response.data)
        })
    }
}
