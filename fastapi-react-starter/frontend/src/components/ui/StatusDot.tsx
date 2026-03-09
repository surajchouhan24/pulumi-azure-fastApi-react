// frontend/src/components/ui/StatusDot.tsx
import React from "react";
import { HealthStatusType } from "../../hooks/useHealthStatus";

interface StatusDotProps {
  status: HealthStatusType; // "healthy" | "error" | "loading"
}

export function StatusDot({ status }: StatusDotProps) {
  const colors: Record<HealthStatusType, string> = {
    healthy: "bg-green-500",
    error: "bg-red-500",
    loading: "bg-gray-300 animate-pulse",
  };

  return <div className={`w-3 h-3 rounded-full mr-2 ${colors[status]}`} />;
}