// import { use } from 'react'
// import { StatusDot } from '../../components/ui/StatusDot'
// import { useHealthStatus } from '../../hooks/useHealthStatus'

// type HealthData = {
//   status: "healthy" | "error" | "loading";
// };

// export function HealthStatus() {
//   // const data = use(useHealthStatus())
//   const data = useHealthStatus() as HealthData;

//   return (
//     <div className="flex items-center">
//       <StatusDot status={data.status} />
//       <span className="text-gray-600">Status: {data.status}</span>
//     </div>
//   )
// }

import { useEffect, useState } from 'react'
import { StatusDot } from '../../components/ui/StatusDot'
import { useHealthStatus } from '../../hooks/useHealthStatus'

type HealthData = {
  status: 'healthy' | 'error' | 'loading'
}

export function HealthStatus() {
  const [data, setData] = useState<HealthData>({ status: 'loading' })

  useEffect(() => {
    useHealthStatus().then((res) => {
      setData(res)
    })
  }, [])

  return (
    <div className="flex items-center">
      <StatusDot status={data.status} />
      <span className="ml-2">Status: {data.status}</span>
    </div>
  )
}
