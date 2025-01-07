const { default: useSWR } = require("swr")


const fetcher = (...args) => fetch(...args).then(res => res.json())

export function useFetch (endpoint) {
    const { data, error, isLoading } = useSWR(endpoint, fetcher)
   
    return {
      data,
      isLoading,
      isError: error
    }
  }