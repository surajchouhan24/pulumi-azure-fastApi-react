// frontend/src/hooks/useHealthStatus.ts
import { useEffect, useState } from 'react'

export type HealthStatusType = 'healthy' | 'error' | 'loading'

interface HealthData {
  status: HealthStatusType
  message?: string
}

export function useHealthStatus() {
  const [data, setData] = useState<HealthData>({ status: 'loading' })

  useEffect(() => {
    let isMounted = true

    async function fetchHealth() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/api/health`)
        if (!response.ok) {
          if (isMounted) setData({ status: 'error' })
          return
        }
        const json: HealthData = await response.json()
        if (isMounted) setData(json)
      } catch (err: unknown) {
        if (isMounted)
          setData({
            status: 'error',
            message: err instanceof Error ? err.message : String(err),
          })
      }
    }

    fetchHealth()

    return () => {
      isMounted = false
    }
  }, [])

  return data
}
