import { useEffect } from 'react'
import commonApi, { IRequestArgs } from 'app/common/api'

const api: { [property: string]: Function } = {
    ...commonApi
}

const promises = new Map()

Object.keys(api).forEach((key) => {
    const method = api[key]

    api[key] = (url: string, args: IRequestArgs) => {
        const abortController = new AbortController()

        const promise = method(url, args, abortController)
            .finally(() => {
                promises.delete(abortController)
            })

        promises.set(abortController, promise)

        return promise
    }
})

export default () => {
    useEffect(() => {
        return () => {
            for (let abortController of promises.keys()) {
                abortController.abort()
            }

            promises.clear()
        }
    }, [])

    return api
}
